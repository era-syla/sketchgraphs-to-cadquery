import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.3645, 0.2345).lineTo(0.3645, 0.2345).lineTo(0.3645, -0.2345).lineTo(-0.3645, -0.2345).lineTo(-0.3645, 0.2345).close()
solid=wp_sketch0.add(loop0).extrude(0.09268782445813795)
