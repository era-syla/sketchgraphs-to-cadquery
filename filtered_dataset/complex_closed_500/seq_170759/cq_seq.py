import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-1.2192, 0.0).lineTo(-1.27, 0.0).lineTo(-1.27, 0.3048).lineTo(-1.26365, 0.3048).threePointArc((-1.2446, 0.28575), (-1.22555, 0.3048)).lineTo(-1.2192, 0.3048).lineTo(-1.2192, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.24212242754406665)
