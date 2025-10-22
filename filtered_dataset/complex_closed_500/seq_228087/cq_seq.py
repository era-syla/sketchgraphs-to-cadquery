import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-1.075, -0.088).lineTo(1.075, -0.088).lineTo(1.075, -0.113).lineTo(-1.075, -0.113).lineTo(-1.075, -0.088).close()
solid=wp_sketch0.add(loop0).extrude(-4.03885470725592)
