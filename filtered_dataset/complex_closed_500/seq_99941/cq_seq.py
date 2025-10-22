import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0293, 0.0238).lineTo(0.0293, 0.0238).lineTo(0.0293, -0.0238).lineTo(-0.0293, -0.0238).lineTo(-0.0293, 0.0238).close()
solid=wp_sketch0.add(loop0).extrude(0.11004905671921363)
