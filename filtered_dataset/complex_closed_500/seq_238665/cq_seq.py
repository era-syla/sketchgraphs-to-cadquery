import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01, 0.0085).lineTo(-0.0085, 0.0085).lineTo(-0.0085, 0.0015).lineTo(-0.01, 0.0015).lineTo(-0.01, 0.0085).close()
solid=wp_sketch0.add(loop0).extrude(-0.012742562149468298)
