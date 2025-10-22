import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.39436, 0.15845).lineTo(-0.39436, -0.19379).lineTo(0.03119, 0.15845).lineTo(-0.39436, 0.15845).close()
solid=wp_sketch0.add(loop0).extrude(1.1271688943578582)
