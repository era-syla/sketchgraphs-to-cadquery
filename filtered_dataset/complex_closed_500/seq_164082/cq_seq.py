import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00889, 0.00191).lineTo(-0.01772, 0.00191).lineTo(-0.01772, -0.00191).lineTo(-0.00889, -0.00191).lineTo(-0.00889, 0.00191).close()
solid=wp_sketch0.add(loop0).extrude(-0.00795197985844185)
