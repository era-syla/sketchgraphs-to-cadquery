import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01032, 0.006).lineTo(-0.01032, -0.00746).lineTo(0.02283, -0.00746).lineTo(0.0, 0.03491).lineTo(-0.01511, 0.01514).lineTo(-0.00432, 0.0069).lineTo(-0.00432, 0.0033).lineTo(-0.00732, 0.0033).lineTo(-0.00732, 0.006).lineTo(-0.01032, 0.006).close()
solid=wp_sketch0.add(loop0).extrude(0.10954246478832512)
