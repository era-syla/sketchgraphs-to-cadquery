import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02468, 0.0332).lineTo(-0.02468, -0.05354).lineTo(0.04472, -0.05354).lineTo(0.04472, -0.00957).lineTo(0.01002, 0.0332).lineTo(-0.02468, 0.0332).close()
solid=wp_sketch0.add(loop0).extrude(-0.1330016082623787)
