import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.09802, -0.01825).lineTo(-0.08102, -0.01825).lineTo(-0.08102, -0.00125).lineTo(-0.09802, -0.00125).lineTo(-0.09802, -0.01825).close()
solid=wp_sketch0.add(loop0).extrude(-0.01318442843966721)
