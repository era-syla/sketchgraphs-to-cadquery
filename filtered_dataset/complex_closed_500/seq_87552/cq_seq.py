import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03769, -0.02202).lineTo(-0.02245, -0.02202).lineTo(-0.02245, -0.03218).lineTo(-0.03769, -0.03218).lineTo(-0.03769, -0.02202).close()
solid=wp_sketch0.add(loop0).extrude(-0.012131386344238956)
