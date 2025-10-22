import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.04543, 0.1163).lineTo(-0.04543, 0.1163).lineTo(-0.04543, 0.11037).lineTo(0.04543, 0.11037).lineTo(0.04543, 0.1163).close()
solid=wp_sketch0.add(loop0).extrude(0.1993847461631244)
