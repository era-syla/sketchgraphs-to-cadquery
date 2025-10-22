import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.07378, -0.01877).lineTo(0.06267, -0.01877).lineTo(0.06267, 0.00505).lineTo(0.07378, 0.00505).lineTo(0.07378, -0.01877).close()
solid=wp_sketch0.add(loop0).extrude(0.00725819993242617)
