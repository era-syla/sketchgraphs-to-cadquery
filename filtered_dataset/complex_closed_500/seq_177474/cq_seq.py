import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01416, 0.05046).lineTo(0.02819, 0.05046).lineTo(0.02819, 0.03827).lineTo(0.01416, 0.03827).lineTo(0.01416, 0.05046).close()
solid=wp_sketch0.add(loop0).extrude(-0.03307492884143774)
