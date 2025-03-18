# Create tab content
tab_contents = [widgets.Output(), widgets.Output()]

# Display the DataFrame in the first tab
with tab_contents[0]:
    display(df)

# Add some content to the second tab
with tab_contents[1]:
    print("This is the second tab.")

# Create the tab widget
tab = widgets.Tab(children=tab_contents)
tab.set_title(0, 'DataFrame')
tab.set_title(1, 'Other Info')

# Display the tabs
display(tab)
