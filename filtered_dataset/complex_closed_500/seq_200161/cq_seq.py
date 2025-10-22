import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.07064, 0.00318).lineTo(-0.06112, 0.00318).lineTo(-0.06112, -0.00317).lineTo(-0.07064, -0.00317).lineTo(-0.07064, 0.00318).close()
solid=wp_sketch0.add(loop0).extrude(-0.006262575987332992)
