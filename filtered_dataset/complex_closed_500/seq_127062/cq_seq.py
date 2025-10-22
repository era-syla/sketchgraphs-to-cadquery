import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.5, -0.283).lineTo(-0.518, -0.283).lineTo(-0.518, 0.317).lineTo(-0.5, 0.317).lineTo(-0.5, -0.283).close()
solid=wp_sketch0.add(loop0).extrude(-0.511507622490513)
