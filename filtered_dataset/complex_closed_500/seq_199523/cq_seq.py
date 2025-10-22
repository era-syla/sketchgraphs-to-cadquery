import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.03, 0.035).lineTo(-0.03, 0.035).lineTo(-0.03, -0.035).lineTo(0.03, -0.035).lineTo(0.03, 0.035).close()
solid=wp_sketch0.add(loop0).extrude(-0.02771973649164184)
