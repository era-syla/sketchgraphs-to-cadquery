import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.036, 4.96174).lineTo(4.964, 4.96174).lineTo(4.964, -0.03826).lineTo(-0.036, -0.03826).lineTo(-0.036, 4.96174).close()
solid=wp_sketch0.add(loop0).extrude(-11.536947644827432)
