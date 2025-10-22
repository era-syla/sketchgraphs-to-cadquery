import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.051, -0.01753).lineTo(0.051, -0.01753).lineTo(0.051, -0.01253).lineTo(-0.051, -0.01253).lineTo(-0.051, -0.01753).close()
solid=wp_sketch0.add(loop0).extrude(0.19931757397512173)
