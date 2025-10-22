import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.05208, 0.04423).lineTo(-0.05208, 0.04423).lineTo(-0.05208, -0.04423).lineTo(0.05208, -0.04423).lineTo(0.05208, 0.04423).close()
solid=wp_sketch0.add(loop0).extrude(-0.06773239984618594)
