import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00475, -0.0025).lineTo(-0.00475, -0.0025).lineTo(-0.00475, 0.0025).lineTo(0.00475, 0.0025).lineTo(0.00475, 0.001).lineTo(-0.00375, 0.0005).lineTo(-0.00375, -0.0005).lineTo(0.00475, -0.001).lineTo(0.00475, -0.0025).close()
solid=wp_sketch0.add(loop0).extrude(-0.018012199942254732)
