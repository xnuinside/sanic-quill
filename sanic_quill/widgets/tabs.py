from wtforms import widgets


class TabWidget(object):
    
    def __init__(self, tabs=None, wysiwyg_fields=None, tabs_field='language'):

        self.tabs = tabs if tabs else []
        self.wysiwyg_fields = wysiwyg_fields or ['content']
        self.tabs_field = tabs_field

    def __call__(self, fields, **kwargs):
        kwargs.setdefault('id', fields.id)
        
        if kwargs.get('class'):
            kwargs['class'] += ' tabwidget'
        else:
            kwargs.setdefault('class', 'tabwidget')

        html = ['<div class="tab">']
        
        for tab in self.tabs:
            html.append("""<button type='button' class='tablinks' onclick='openTab(event, "{}")'>
{}</button>""".format(tab[0], tab[1]))
        html.append('</div>')

        for index, tab in enumerate(self.tabs):
            subfield = fields[index]
            hidden_inputs = []
            for wysiwyg_field in self.wysiwyg_fields:
                content_id = "{}-{}".format(subfield.id, wysiwyg_field)
                hidden_inputs.append("""<input type='hidden' id='hidden-{}' name='{}' value='{}'>""".format(
                    content_id, content_id, subfield.data[wysiwyg_field]
                ))
            subfield.id = "{}-{}__{}".format(subfield.id, self.tabs_field, tab[0])
            html.append("""<div id='{}' class='tabcontent'>
{}</div>{}""".format(
                tab[0],
                subfield(),
                ''.join(hidden_inputs)                
                )
            )

        html.append('</div>')
        # todo widgets.HTMLString deprecated, need to change
        result = widgets.HTMLString(''.join(html))
        return result
