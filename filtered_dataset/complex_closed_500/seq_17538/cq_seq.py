import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, -3.29697).lineTo(0.6, -3.29697).lineTo(0.6, -2.34897).lineTo(-0.0, -2.34897).lineTo(0.0, -3.29697).close()
solid=wp_sketch0.add(loop0).extrude(1.5491716862367328)
