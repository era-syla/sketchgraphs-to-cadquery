import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04, -0.2995).lineTo(-0.04, -0.2995).lineTo(-0.04, 0.2995).lineTo(0.04, 0.2995).lineTo(0.04, -0.2995).close()
solid=wp_sketch0.add(loop0).extrude(-1.2014238995541937)
