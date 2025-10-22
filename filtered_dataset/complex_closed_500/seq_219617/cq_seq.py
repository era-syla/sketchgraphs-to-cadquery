import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.06137, -0.05569).lineTo(-0.06137, -0.05569).lineTo(-0.06137, 0.05569).lineTo(0.06137, 0.05569).lineTo(0.06137, -0.05569).close()
solid=wp_sketch0.add(loop0).extrude(0.12671860202024415)
