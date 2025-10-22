import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.06985, 0.06985).lineTo(0.06985, 0.06985).lineTo(0.06985, -0.06985).lineTo(-0.06985, -0.06985).lineTo(-0.06985, 0.06985).close()
solid=wp_sketch0.add(loop0).extrude(0.07275552922745576)
