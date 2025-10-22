import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04256, 0.02509).lineTo(-0.05056, 0.02509).lineTo(-0.05056, 0.02909).lineTo(-0.04256, 0.02909).threePointArc((-0.03256, 0.02609), (-0.02256, 0.02909)).lineTo(-0.01456, 0.02909).lineTo(-0.01456, 0.02509).lineTo(-0.02256, 0.02509).threePointArc((-0.03256, 0.02264), (-0.04256, 0.02509)).close()
solid=wp_sketch0.add(loop0).extrude(0.06609779390435232)
