import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0671, 0.1383).lineTo(-0.0, 0.1383).lineTo(0.0, 0.0).lineTo(-0.0671, 0.0).lineTo(-0.0671, 0.1383).close()
solid=wp_sketch0.add(loop0).extrude(-0.009360732450874223)
