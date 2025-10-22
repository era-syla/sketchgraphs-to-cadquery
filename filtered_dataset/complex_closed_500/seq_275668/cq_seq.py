import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.015, 0.017).lineTo(0.021, 0.017).lineTo(0.021, 0.007).lineTo(0.015, 0.013).lineTo(0.015, 0.017).close()
solid=wp_sketch0.add(loop0).extrude(0.0012551114368462104)
