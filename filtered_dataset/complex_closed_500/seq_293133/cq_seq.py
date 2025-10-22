import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0094, -0.00304).lineTo(-0.04961, -0.00304).lineTo(-0.04961, -0.00373).threePointArc((-0.04924, -0.00463), (-0.04834, -0.005)).lineTo(-0.0094, -0.005).lineTo(-0.0094, -0.00304).close()
solid=wp_sketch0.add(loop0).extrude(-0.10062222107924786)
