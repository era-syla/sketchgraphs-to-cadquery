import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.08861, 0.07457).lineTo(0.08981, 0.07457).lineTo(0.08981, -0.12972).lineTo(-0.08861, -0.12972).lineTo(-0.08861, 0.07457).close()
solid=wp_sketch0.add(loop0).extrude(0.42614333060253823)
