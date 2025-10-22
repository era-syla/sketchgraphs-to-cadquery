import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.00714).lineTo(-0.038, 0.00714).lineTo(-0.038, 0.0).lineTo(0.0, 0.0).lineTo(0.0127, 0.0).lineTo(0.0127, 0.00635).lineTo(0.014, 0.00635).lineTo(0.014, 0.01).lineTo(0.007, 0.01).lineTo(0.007, 0.0143).lineTo(0.004, 0.0143).lineTo(0.0, 0.011).lineTo(0.0, 0.00714).close()
solid=wp_sketch0.add(loop0).extrude(-0.03932135803099243)
