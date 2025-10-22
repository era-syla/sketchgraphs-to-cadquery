import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.2425, 0.7108).lineTo(0.2575, 0.7108).lineTo(0.2575, 0.1608).lineTo(0.2425, 0.1608).lineTo(0.2425, 0.7108).close()
solid=wp_sketch0.add(loop0).extrude(-0.1830848816695325)
