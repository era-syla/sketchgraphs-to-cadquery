import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05769, 0.07663).lineTo(0.0817, 0.07663).lineTo(0.0817, -0.06275).lineTo(-0.05769, -0.06275).lineTo(-0.05769, 0.07663).close()
solid=wp_sketch0.add(loop0).extrude(0.22992247798584503)
