import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00525, 0.0072).lineTo(-0.00575, 0.0072).lineTo(-0.01025, -0.00925).lineTo(-0.00994, -0.00933).lineTo(-0.00551, 0.00688).lineTo(-0.00525, 0.00688).lineTo(-0.00525, 0.0072).close()
solid=wp_sketch0.add(loop0).extrude(0.025426188051610246)
