import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.17812, 1.10591).threePointArc((-0.1745, 1.119), (-0.17812, 1.13209)).threePointArc((-0.18179, 1.13448), (-0.18594, 1.13306)).lineTo(-0.18621, 1.13279).threePointArc((-0.1805, 1.119), (-0.18621, 1.10521)).lineTo(-0.18594, 1.10494).threePointArc((-0.18179, 1.10352), (-0.17812, 1.10591)).close()
solid=wp_sketch0.add(loop0).extrude(0.035493747638019754)
