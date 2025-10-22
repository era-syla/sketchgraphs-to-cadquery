import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03, -0.0).lineTo(-0.03, 0.052).lineTo(-0.018, 0.052).lineTo(-0.018, 0.012).lineTo(0.028, 0.012).lineTo(0.028, 0.0).lineTo(-0.03, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.08913827227061404)
