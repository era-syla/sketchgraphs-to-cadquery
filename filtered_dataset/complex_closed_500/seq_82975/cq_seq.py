import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0519, 0.04962).lineTo(-0.0481, 0.04962).lineTo(-0.0481, -0.02538).lineTo(0.0519, -0.02538).lineTo(0.0519, 0.04962).close()
solid=wp_sketch0.add(loop0).extrude(-0.07809984999586309)
