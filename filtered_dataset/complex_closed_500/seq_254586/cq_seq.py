import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01772, -0.03872).lineTo(-0.02822, -0.03872).lineTo(-0.02822, -0.07265).lineTo(-0.01772, -0.07265).lineTo(-0.01772, -0.03872).close()
solid=wp_sketch0.add(loop0).extrude(-0.01371994193157635)
