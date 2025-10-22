import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01257, 0.01257).lineTo(0.01257, 0.01257).lineTo(0.01257, -0.01257).lineTo(-0.01257, -0.01257).lineTo(-0.01257, 0.01257).close()
solid=wp_sketch0.add(loop0).extrude(-0.07481009585606291)
