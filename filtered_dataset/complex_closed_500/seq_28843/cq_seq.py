import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0186, 0.0118).lineTo(-0.0186, 0.0118).threePointArc((-0.02086, 0.01086), (-0.0218, 0.0086)).lineTo(-0.0218, -0.0086).threePointArc((-0.02086, -0.01086), (-0.0186, -0.0118)).lineTo(0.0186, -0.0118).threePointArc((0.02086, -0.01086), (0.0218, -0.0086)).lineTo(0.0218, 0.0086).threePointArc((0.02086, 0.01086), (0.0186, 0.0118)).close()
solid=wp_sketch0.add(loop0).extrude(-0.032696196576995094)
