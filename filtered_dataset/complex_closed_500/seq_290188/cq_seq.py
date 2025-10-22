import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01995, -0.006).lineTo(-0.01995, 0.0029).lineTo(-0.01864, 0.0029).lineTo(-0.01864, 0.00018).lineTo(0.01864, 0.00018).lineTo(0.01864, 0.0029).lineTo(0.01995, 0.0029).lineTo(0.01995, -0.006).lineTo(-0.01995, -0.006).close()
solid=wp_sketch0.add(loop0).extrude(-0.0830607129982292)
