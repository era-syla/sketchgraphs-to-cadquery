import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.10893, 0.01805).lineTo(-0.10487, 0.01805).lineTo(-0.10487, 0.01598).threePointArc((-0.10563, 0.01592), (-0.10621, 0.01541)).threePointArc((-0.10743, 0.01432), (-0.10893, 0.01499)).lineTo(-0.10893, 0.01805).close()
solid=wp_sketch0.add(loop0).extrude(-0.007570268720073626)
