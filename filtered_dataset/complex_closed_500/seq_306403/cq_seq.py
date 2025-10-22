import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-2.032, 1.5494).lineTo(-1.9939, 1.5494).lineTo(-1.9939, 1.4605).lineTo(-2.032, 1.4605).lineTo(-2.032, 1.5494).close()
solid=wp_sketch0.add(loop0).extrude(0.01968086602227731)
