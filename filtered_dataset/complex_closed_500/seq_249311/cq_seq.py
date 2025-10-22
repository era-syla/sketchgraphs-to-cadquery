import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.1, -0.09774).lineTo(-0.084, -0.09774).lineTo(-0.084, -0.08134).lineTo(-0.1, -0.08134).lineTo(-0.1, -0.09774).close()
solid=wp_sketch0.add(loop0).extrude(-0.02292303931209247)
