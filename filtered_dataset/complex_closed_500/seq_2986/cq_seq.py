import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0386, 0.06457).lineTo(0.09998, 0.06457).lineTo(0.09998, -0.06457).lineTo(-0.0386, -0.06457).lineTo(-0.0386, 0.06457).close()
solid=wp_sketch0.add(loop0).extrude(0.3827646192001151)
