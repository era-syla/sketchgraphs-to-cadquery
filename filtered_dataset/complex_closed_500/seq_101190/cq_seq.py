import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-3.54835, 1.9939).lineTo(-2.61107, 1.9939).lineTo(-2.61107, 0.4953).lineTo(-3.54835, 0.4953).lineTo(-3.54835, 1.9939).close()
solid=wp_sketch0.add(loop0).extrude(0.6927506153202695)
