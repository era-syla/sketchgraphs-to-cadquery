import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05207, 0.04443).lineTo(-0.05207, 0.03781).lineTo(-0.05018, 0.03945).lineTo(-0.0517, 0.04476).lineTo(-0.05207, 0.04443).close()
solid=wp_sketch0.add(loop0).extrude(-0.0026466878556848975)
