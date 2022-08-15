import datapane as dp

# Build report
report = dp.Report("Datapane template")
report.save(path="template.html", open=True)