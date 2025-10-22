import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.08412, -0.0023).lineTo(0.01188, -0.0023).lineTo(0.01188, -0.0983).lineTo(-0.08412, -0.0983).lineTo(-0.08412, -0.0023).close()
solid=wp_sketch0.add(loop0).extrude(0.2557174968472968)
