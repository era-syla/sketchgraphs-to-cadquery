import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.42545, 0.3048).lineTo(0.42545, 0.3048).lineTo(0.42545, 0.2921).lineTo(-0.42545, 0.2921).lineTo(-0.42545, 0.3048).close()
solid=wp_sketch0.add(loop0).extrude(-2.5421047467093016)
