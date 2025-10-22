import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(1.5, -1.28).lineTo(-1.5, -1.28).lineTo(-1.5, 1.28).lineTo(1.5, 1.28).lineTo(1.5, -1.28).close()
solid=wp_sketch0.add(loop0).extrude(5.7059717754042545)
